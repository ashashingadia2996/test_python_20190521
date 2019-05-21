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

def testVerifySafeToSendEmail():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('safe-to-send@example.com')
    
    assert 200 == response.code
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
        
def testVerifyFreeEmail():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('free@example.com')
    
    assert 200 == response.code
    assert 'valid' == response.body['result']
    assert 'accepted_email' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'true' == response.body['free']
    assert 'free@example.com' == response.body['email']
    assert 'free' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'true' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyRejectedEmail():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('rejected-email@example.com')
    
    assert 200 == response.code
    assert 'invalid' == response.body['result']
    assert 'rejected_email' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'rejected-email@example.com' == response.body['email']
    assert 'rejected-email' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyInvalidDomain():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('invalid-domain@example.com')
    
    assert 200 == response.code
    assert 'invalid' == response.body['result']
    assert 'invalid_domain' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'invalid-domain@example.com' == response.body['email']
    assert 'invalid-domain' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert '' == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyInvalidEmail():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('invalid-email@example.com')
    
    assert 200 == response.code
    assert 'invalid' == response.body['result']
    assert 'invalid_email' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'invalid-email@example.com' == response.body['email']
    assert 'invalid-email' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert '' == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyExceededStorage():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('exceeded-storage@example.com')
    
    assert 200 == response.code
    assert 'invalid' == response.body['result']
    assert 'exceeded_storage' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'exceeded-storage@example.com' == response.body['email']
    assert 'exceeded-storage' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyNoMXRecord():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('no-mx-record@example.com')
    
    assert 200 == response.code
    assert 'invalid' == response.body['result']
    assert 'no_mx_record' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'no-mx-record@example.com' == response.body['email']
    assert 'no-mx-record' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert '' == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyDidYouMean():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('did-you-mean@example.com')
    
    assert 200 == response.code
    assert 'invalid' == response.body['result']
    assert 'rejected_email' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'did-you-mean@example.com' == response.body['email']
    assert 'did-you-mean' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert 'did-you-mean@example.com' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyTimeout():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('timeout@example.com')
    
    assert 200 == response.code
    assert 'unknown' == response.body['result']
    assert 'timeout' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'timeout@example.com' == response.body['email']
    assert 'timeout' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyUnexpectedError():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('unexpected-error@example.com')
    
    
    assert 200 == response.code
    assert 'unknown' == response.body['result']
    assert 'unexpected_error' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'unexpected-error@example.com' == response.body['email']
    assert 'unexpected-error' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyNoConnect():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('no-connect@example.com')
    
    assert 200 == response.code
    assert 'unknown' == response.body['result']
    assert 'no_connect' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'no-connect@example.com' == response.body['email']
    assert 'no-connect' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyUnavailableSMTP():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('unavailable-smtp@example.com')
    
    assert 200 == response.code
    assert 'unknown' == response.body['result']
    assert 'unavailable_smtp' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'unavailable-smtp@example.com' == response.body['email']
    assert 'unavailable-smtp' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyTemporarilyBlocked():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('temporarily-blocked@example.com')
    
    assert 200 == response.code
    assert 'unknown' == response.body['result']
    assert 'temporarily_blocked' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'temporarily-blocked@example.com' == response.body['email']
    assert 'temporarily-blocked' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyAcceptAll():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('accept-all@example.com')
    
    assert 200 == response.code
    assert 'valid' == response.body['result']
    assert 'accepted_email' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'true' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'accept-all@example.com' == response.body['email']
    assert 'accept-all' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
        
def testVerifyRole():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('role@example.com')
    
    assert 200 == response.code
    assert 'valid' == response.body['result']
    assert 'accepted_email' == response.body['reason']
    assert 'false' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'true' == response.body['role']
    assert 'false' == response.body['free']
    assert 'role@example.com' == response.body['email']
    assert 'role' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
    
def testVerifyDisposable():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('disposable@example.com')
    
    assert 200 == response.code
    assert 'valid' == response.body['result']
    assert 'accepted_email' == response.body['reason']
    assert 'true' == response.body['disposable']
    assert 'false' == response.body['accept_all']
    assert 'false' == response.body['role']
    assert 'false' == response.body['free']
    assert 'disposable@example.com' == response.body['email']
    assert 'disposable' == response.body['user']
    assert 'example.com' == response.body['domain']
    assert None == response.body['mx_record']
    assert '' == response.body['mx_domain']
    assert 'false' == response.body['safe_to_send']
    assert '' == response.body['did_you_mean']
    assert 'true' == response.body['success']
    
def testVerifyLowCredit():
    client = evm.Client(os.getenv('apikey'))
    evm1 = client.evm()
    
    response = evm1.sandbox('low-credit@example.com')
    
    assert 402 == response.code
