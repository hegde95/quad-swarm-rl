from sample_factory.runner.run_description import RunDescription, Experiment, ParamGrid

from swarm_rl.runs.quad_multi_deepsets_obstacle_baseline import QUAD_8_OBSTACLES_PARAMETERZE_CLI, seeds

_params = ParamGrid([
    ('seed', seeds(2)),
    ('quads_obstacle_type', ['cylinder']),
    ('lr_schedule', ['kl_adaptive_epoch']),
    ('lr_schedule_kl_threshold', [0.008]),
    ('policy_initialization', ['torch_default']),
    ('kl_loss_coeff', [0.1]),
    ('exploration_loss_coeff', [0.0])
])

SMALL_MODEL_CLI = QUAD_8_OBSTACLES_PARAMETERZE_CLI + (
    ' --hidden_size=16 --quads_neighbor_hidden_size=8 --quads_obstacle_hidden_size=8 --with_wandb=False'
)

_experiment = Experiment(
    'v2-cylinder-small_model',
    SMALL_MODEL_CLI,
    _params.generate_params(randomize=False),
)

RUN_DESCRIPTION = RunDescription('8_obst_2_local_quads_multi_obst_mix_8a_v116', experiments=[_experiment])

# On Brain server, when you use num_workers = 72, if the system reports: Resource temporarily unavailable,
# then, try to use two commands below
# export OMP_NUM_THREADS=1
# export USE_SIMPLE_THREADED_LEVEL3=1

# Command to use this script on server:
# xvfb-run python -m runner.run --run=quad_multi_through_hole_obstacle --runner=processes --max_parallel=4 --pause_between=1 --experiments_per_gpu=1 --num_gpus=4
# Command to use this script on local machine:
# Please change num_workers to the physical cores of your local machine
# python -m runner.run --run=quad_multi_through_hole_obstacle --runner=processes --max_parallel=4 --pause_between=1 --experiments_per_gpu=1 --num_gpus=4

# Slurm
# srun --exclusive -c72 -N1 --gres=gpu:4 python -m sample_factory.runner.run --run=swarm_rl.runs.quad_multi_deepsets_through_random_obstacles --runner=processes --max_parallel=4 --pause_between=1 --experiments_per_gpu=1 --num_gpus=4