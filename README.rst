aws-profile
===========

Wrapper script to generate and pass AWS AssumeRole keys to other scripts


Usage
-----

There are two primary ways to use **aws-profile**, inline and with environment variables.

**Inline Profile Name**

`aws-profile <profile> <command>`

**Profile Environment Variable**

`AWS_PROFILE='<profile>' aws-profile <command>`


Options
-------

**AWS_CACHE**: Set the AWS_CACHE environment variable to control caching.
Use `AWS_CACHE=false` to disable caching, or any other value
(or unset) to keep caching enabled. When set to false the MFA
code will be requested every time.

Configuring Profiles
--------------------

`aws-profile` uses the built in profiles from the AWS CLI. For full details see `Named Profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-multiple-profiles.html>`_ in the AWS Documentation.

Here is an example of how to configure a profile for a role, with MFA::

    [profile my_profile]
    role_arn = arn:aws:iam::<account_id>:role/<role_name>
    source_profile = default
    mfa_serial = arn:aws:iam::<account_id>:mfa/<username>

Where `<account_id>` is your AWS Account ID, `<role_name>` is the name of the role you want to assume, and `<username>` is the username of the AWS User used fo your default profile.
