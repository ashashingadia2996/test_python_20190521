import evm
import pytest
import os

def testVerifyValidEmail():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('valid@example.com')
    
    assert 200 == response.code
    assert 'valid' == response.body['result']
    assert 'accepted_email' == response.body['reason']
    assert 'true' == response.body['disposable']
    assert 'true' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'valid@example.com' == response.body['email']
    assert 'valid' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']

def test_VerifySafeToSendEmail():
	client = evm.Client(os.getenv('apikey'))
	evm1 = client.evm()

	response = evm1.sandbox('safe-to-send@example.com')
	assert 'valid' == response.body['result']
	assert 'accepted_email' == response.body['reason']
	assert 'false' == response.body['disposable']
	assert 'false' == response.body['accept_all']
	assert 'false' == response.body['role']
	assert 'false' == response.body['free']
	assert 'safe-to-send@example.com' == response.body['email']
	assert 'safe-to-send' == response.body['user']
	assert 'example.com' == response.body['domain']
	assert None == response.body['mx_record']
	assert '' == response.body['mx_domain']
	assert 'true' == response.body['safe_to_send']
	assert '' == response.body['did_you_mean']
	assert 'true' == response.body['success']