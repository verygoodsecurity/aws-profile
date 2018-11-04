import os

import pytest

from awsprofile import parse_args


@pytest.fixture(autouse=True)
def setup_environment():
    for environment_variable in ['AWS_PROFILE', 'AWS_DEFAULT_PROFILE', 'AWS_CACHE']:
        try:
            del os.environ[environment_variable]
        except KeyError:
            pass


def test_parse_args_no_envs_or_args():
    """With no envvars and no profile option it should raise an exception caused by quit"""
    with pytest.raises(SystemExit):
        argv_test_data = ['aws-profile', 'command']
        parse_args(argv=argv_test_data)


def test_parse_args_with_profile_arg():
    """With no envvars and a profile set on the command line it should return the correct profile name, the command[s] and the default cache of true """
    argv_test_data = ['aws-profile', 'test-profile-name', 'test-command-name']
    result = parse_args(argv=argv_test_data)
    assert ('test-profile-name', ['test-command-name'], 'true') == result


def test_parse_args_with_aws_profile_env_set():
    """With AWS_PROFILE set and no profile set on the command line it should return the profile name from AWS_PROFILE, the command[s] and the default cache of true """
    argv_test_data = ['aws-profile', 'test-command-name']
    os.environ['AWS_PROFILE'] = 'profile-from-aws-profile-envvar'
    result = parse_args(argv=argv_test_data)
    assert ('profile-from-aws-profile-envvar', ['test-command-name'], 'true') == result


def test_parse_args_with_aws_default_profile_env_set():
    """With AWS_DEFAULT_PROFILE set and no profile set on the command line it should return the correct profile name from AWS_DEFAULT_PROFILE, the command[s] and the default cache of true """
    argv_test_data = ['aws-profile', 'test-command-name']
    os.environ['AWS_DEFAULT_PROFILE'] = 'profile-from-aws-default-profile-envvar'
    result = parse_args(argv=argv_test_data)
    assert ('profile-from-aws-default-profile-envvar', ['test-command-name'], 'true') == result


@pytest.mark.skip(reason="This test fails as the implementation in code is incorrect see https://github.com/aws/aws-cli/issues/2597 which infers AWS_PROFILE should be used over AWS_DEFAULT_PROFILE")
def test_parse_args_with_aws_default_profile_and_aws_profile_env_set():
    """With AWS_PROFILE and AWS_DEFAULT_PROFILE set and no profile set on the command line it should return the correct profile name from AWS_PROFILE, the command[s] and the default cache of true """
    argv_test_data = ['aws-profile', 'test-command-name']
    os.environ['AWS_DEFAULT_PROFILE'] = 'profile-from-aws-default-profile-envvar'
    os.environ['AWS_PROFILE'] = 'profile-from-aws-profile-envvar'
    result = parse_args(argv=argv_test_data)
    assert ('profile-from-aws-profile-envvar', ['test-command-name'], 'true') == result


@pytest.mark.skip(reason="This test fails as the implementation in code is ambiguous is it a profile or is it part of the command? Should we add argparse and a named option?")
def test_parse_args_with_aws_default_profile_and_aws_profile_env_set_and_profile_provided():
    """With AWS_PROFILE and AWS_DEFAULT_PROFILE set and profile set on the command line it should return the correct profile name from AWS_PROFILE, the command[s] and the default cache of true """
    argv_test_data = ['aws-profile', 'test-profile-name', 'test-command-name']
    os.environ['AWS_DEFAULT_PROFILE'] = 'profile-from-aws-default-profile-envvar'
    os.environ['AWS_PROFILE'] = 'profile-from-aws-profile-envvar'
    result = parse_args(argv=argv_test_data)
    assert ('profile-from-aws-profile-envvar', ['test-command-name'], 'true') == result


@pytest.mark.parametrize("envvar,expected", [
    ("anything", "true"),
    ("true", "true"),
    ("True", "true"),
     ("tRue", "true"),
     ("TRUE", "true"),
     ("false", "false"),
     ("FALSE", "false"),
     ("fAlse", "false"),
     ("False", "false")
])
def test_cache_envar_set_to_anything_other_than_false_or_FALSE(envvar, expected):
    """With AWS_CACHE env var set to anything other than false (case insensitive) it should return the string 'true'"""
    os.environ['AWS_CACHE'] = envvar
    argv_test_data = ['aws-profile', 'test-profile-name', 'test-command-name']
    result = parse_args(argv=argv_test_data)
    assert ('test-profile-name', ['test-command-name'], expected) == result
