def overwrite(GD, population, iteration, mutation):
    config_file = open("config.py", 'w+')
    config = ['', '', '', '']
    config[0] = f'GD = {GD}\n'
    config[1] = f'population_size = {population}\n'
    config[2] = f'iterations_size = {iteration}\n'
    config[3] = f'mutation_size = {mutation}\n'

    config_file.writelines(config)
    # print(config)