import pytest

import awsprofile


def test_configure_cache(mocker):
    mock_provider = mocker.Mock()
    mock_provider.cache = None
    mock_cred_chain = mocker.Mock()
    mock_cred_chain.get_provider.return_value = mock_provider
    mock_session = mocker.Mock()
    mock_session.get_component.return_value = mock_cred_chain
    awsprofile.configure_cache(mock_session)
    mock_session.get_component.assert_called_with('credential_provider')
    mock_cred_chain.get_provider.called_with('assume-role')
    assert isinstance(mock_provider.cache, awsprofile.FixedJSONFileCache)
