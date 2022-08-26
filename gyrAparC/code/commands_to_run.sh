#!/bin/bash
#SBATCH -J sdemmou_gyrA_parC # job name
#SBATCH -p workq # partition to use
#SBATCH --mem=100G
#SBATCH --cpus-per-task=10


module load bioinfo/snakemake-5.25.0

#snakemake -n -r 

#snakemake --cluster "sbatch -A {cluster.account} -t {cluster.time} -p {cluster.partition} -N {cluster.nodes}" --cluster-config cluster_config.yml --jobs 10 --use-envmodules --unlock

snakemake --cluster "sbatch -A {cluster.account} -t {cluster.time} -p {cluster.partition} -N {cluster.nodes}" --cluster-config cluster_config.yml --jobs 10 --use-envmodules --rerun-incomplete
