from setuptools import setup, find_packages

setup(
    name='neural_decoder',
    version='0.0.1',
    packages=find_packages(include=['neuralDecoder']),
    install_requires=[
        'tensorflow-gpu==2.7.0',
        # 'tensorflow-gpu==2.12.0',
        'hydra-core==1.3.2',
        'hydra-submitit-launcher==1.1.5',
        'hydra-optuna-sweeper==1.2.0',
        'transformers==4.28.1',
        'redis',
        'seaborn',
        'pandas',
        'jupyterlab',
        'ipywidgets',
        'tqdm',
        'g2p_en==2.1.0',
        'seaborn==0.12.2',
        'numpy==1.25.0',
        'scipy==1.11.1',
        'torch==1.13.1',
        'accelerate==0.20.3',
        'bitsandbytes==0.39.1',
        'edit_distance==1.0.6',
        'wandb==0.15.5',
        'hiplot',
        'numba',
        'scikit-learn'
    ]
)
