# vgs-aws-profile

### Usage

There are two primary ways to use **aws-profile**, inline using arguments and with environment variables.

**Inline Profile Name**

`vgs-aws-profile [-p, --profile <profile name>] [-r, --region <region>] <command>`

**Profile Environment Variable**

`vgs-aws-profile -p dev -r us-east-1 <command>`

### Install

```
pip install vgs-aws-profile
```

### Release new version

python setup.py sdist
python setup.py install
python setup.py develop
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*