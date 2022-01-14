from __future__ import print_function
import os
import neat
import bees_neural
import random


gW = 7
roomCount = 3

def eval_genomes(genomes, config):
    school = [0 for i in range(gW**2)]
    for i in range(roomCount): school[random.randint(0,gW**2-1)] = 1
    cnt = 0
    outie = []
    fitTop = 0
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        output = net.activate(school)
        output = [0 if x<.5 else 1 for x in output]
        genome.fitness = (1 - 2*(bees_neural.countConnected(school,output,gW)/gW**2) if bees_neural.isFullyConnected(school, output, gW) else .25*bees_neural.countConnected(school,output,gW)/gW**2)
        if genome.fitness > fitTop: 
            outie = output
            fitTop = genome.fitness
    bees_neural.draw(school,outie,gW)
    print(fitTop,"----")

def run(config_file):
    # Load configuration.
    print('running?')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    print('boop')
    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    print('hereo')
    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    print('here')
    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 1000)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    
    school = [0 for i in range(gW**2)]
    for i in range(roomCount): school[random.randint(0,gW**2-1)]
    output = winner_net.activate(school)
    bees_neural.draw(school,output,gW)

    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    p.run(eval_genomes, 10)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    run(config_path)