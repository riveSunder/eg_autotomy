# Adaptive autotomy in co-evolved soft body/policy agents

## Setup (Linux)

```
virtualenv my_env --python=python3.8
source my_env/bin/activate
```

### Evogym and dependencies

You'll need some developer tools if they're not already installed on your system.

```
sudo apt-get install -y xorg-dev libglu1-mesa-dev cmake libglew-dev libopenmpi-dev build-essential swig 
# to save mp4s
sudo apt-get install -y ffmpeg
```

Next you'll need to install a few python packages. The commit hashes corrspond to those used for our experiments. 

```
git clone git@github.com:yunshengtian/GPyOpt.git
cd GPyOpt
git checkout 5fc1188ffdefea9a3bc7964a9414d4922603e904
pip install -e .
cd ../

git clone git@github.com:yunshengtian/neat-python.git
cd neat-python
git checkout 2762ab630838520ca6c03a866e8a158f592b0370
pip install -e .
cd ../
```

```
git clone git@github.com:riveSunder/eg_autotomy.git
cd eg_autotomy
git checkout 8a5132f69c60dacb10d292e23fcf160d6745a4d2
pip install -r requirements.txt
cd ../
```

```
git clone --recurse-submodules git@github.com:EvolutionGym/evogym.git
cd evogym
git checkout 9a1a5e7b26702184821e6e64587220ead2ab0e21
pip install -e .
cd ../
```

### eg_autotomy

```
cd eg_autotomy
pip install -e .
```

Run tests

```
python -m eg_tests.test_all
```
