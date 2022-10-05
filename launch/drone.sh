#!/usr/bin/env bash
#SBATCH --gres=gpu:1
#SBATCH -N1
#SBATCH -n1
#SBATCH -c36
#SBATCH --output=tmp/DRONE-%j.log

srun python -m sample_factory.runner.run --run=swarm_rl.runs.quad_single_goal --runner=processes --max_parallel=1 --pause_between=1 --experiments_per_gpu=1 --num_gpus=1
