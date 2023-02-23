#  Non-dominated set generator CLI

## Local installation
This will build the package, and install it directly into your [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).

Using wget
```bash
bash <(wget -qO- https://raw.githubusercontent.com/sanchezcarlosjr/non-dominated-set-generator-cli/main/installer) && cd non-dominated-set-generator-cli && source venv/bin/activate
```
Using curl
```bash
bash <(curl -s https://raw.githubusercontent.com/sanchezcarlosjr/non-dominated-set-generator-cli/main/installer) && cd non-dominated-set-generator-cli && source venv/bin/activate
```

Once installed, you should be able to test the script.

```bash
genset --help
```

``` bash
genset
# Generating non-dominated set (aka pareto front).
# Ready!
```

## Activate virtual environment
```bash
source venv/bin/activate
```

## Plot on gnuplot
```bash
gnuplot -e "plot [0:1][0:1] '$(genset -d 2 -m Sqrt -n Max)'; pause -1"
```

```bash
genset -d 2 -m Sqrt -n Max | xargs -I {} gnuplot -p -e "plot '<cat {}'; pause -1"
```

## Demos
```bash
   genset -d 2 -m Cos -n Max -p 500 | xargs -I {} gnuplot -p -e "plot '<cat {}'; pause -1"
```
![genset demo 1](../demos/genset-d2-mCos-nMax-p500.png)

```bash
   genset -d 2 -m Cos -n Max -p 500 | xargs -I {} gnuplot -p -e "plot [0:1][0:1] '<cat {}'; pause -1"
```
![genset demo 2](../demos/genset-d2-mErf-nMax-p500.png)

```bash
   genset -d 3 -m Erf -n Max -p 500 | xargs -I {} gnuplot -p -e "splot [0:1][0:1][0:1] '<cat {}'; pause -1"
```
![genset demo 3](../demos/genset-d3-mErf-nMax-p500.png)


## Testing

To run the tests, you need to install `pytest`, which is already in the `developer_requirements.txt`.

From the project root, you can run this to test and print all output:

```bash

```

Or to test a specific file or function:

```bash
# Test file tests/test_my_app.py
python -m pytest -s tests/test_my_app.py

# Test function test_app_main() in tests/test_my_app.py
python -m pytest -s tests/test_my_app.py::test_app_main
```


## Versioning

Every time you publish the package (either locally or remote), the `version` field in `publish/config.json` will go up (specifically, the last digit). So `1.2.3` will become `1.2.4`, etc. It will keep going up.

The major and minor versions (the first two digits) can only be changed manually. Change it directly in the file when you need to.

## Related Reading

* [Packaging Python projects](https://packaging.python.org/tutorials/packaging-projects/): A guide explaining how to package Python projects using `setup.py` and `setuptools` (we use this here).
* [argparse](https://docs.python.org/3/library/argparse.html): I use this to "understand" CLI arguments and sub-commands.
* [pytest](https://docs.pytest.org/en/stable/): Testing framework for this project.
