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
gnuplot -e "splot '$(genset -d 3)'; pause -1"
```

## Publish to PyPI

First, you will need to [create an account on PyPI](https://pypi.org/account/register/). Then you need to export your PyPI credentials in the environment variables of your terminal.

I like to do this by just adding the following exports to the `~/.bashrc` (or whichever file, depending on the terminal you are using).

```bash
export PYPI_REPO_USER="YOUR_USERNAME"
export PYPI_REPO_PASS="YOUR_PASSWORD"
```

The publish script will use these environment variables to upload your package to PyPI. Next, you can run the script:

```bash
cd publish
sh ./publish_remote.sh
```

This will build it into a package like so: https://pypi.org/project/pixegami-my-app/. Now you can install it directly with `pip install`.

## Testing

To run the tests, you need to install `pytest`, which is already in the `developer_requirements.txt`.

From the project root, you can run this to test and print all output:

```bash
python -m pytest -s
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
