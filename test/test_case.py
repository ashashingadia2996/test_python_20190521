import evm
import pytest
import os

def test_VerifySafeToSendEmail():
	client = evm.Client(os.getenv('apikey'))
	evm1 = client.evm()

	response = evm1.sandbox('valid@example.com')
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