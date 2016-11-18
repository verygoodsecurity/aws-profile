#!/bin/bash
DOWNLOAD_URL="https://raw.githubusercontent.com/jrstarke/aws-profile/80a591d026910171190a179c5e79d63572a366e8/aws-profile"
DOWNLOAD_SHA="5abcefcacb06f0447772441db6314b7c5ef1f79e6d598afce6a66f6dbb32e270"

mkdir $HOME/bin
cd $HOME/bin

curl https://raw.githubusercontent.com/jrstarke/aws-profile/master/aws-profile -o aws-profile

if ! echo "$DOWNLOAD_SHA *aws-profile" | shasum -a 256 -c -; then
	echo "The SHA value did not match the expected"
	exit 1
fi

chmod 755 aws-profile

if ! grep "export PATH=\$HOME/bin:\$PATH" $HOME/.bash_profile; then
	echo "export PATH=\$HOME/bin:\$PATH" >> $HOME/.bash_profile
fi

echo "aws-profile has been installed."
echo "You will need to manually run"
echo ""
echo "pip install botocore"
