
import requests


class CredentialInfo():
    app_key="Null"
    app_secret="Null"
    bKashUsername="Null"
    bKashPassword="Null"
    baseURL="http://127.0.0.1:8000/"
    bKashURL="Null"
    createURL="Null"
    authorization="Null"


    def setCredendial(self,appKey,appSecret,username,password):
        self.app_key=appKey
        self.app_secret=appSecret
        self.bKashUsername=username
        self.bKashPassword=password


    def sandbox(self):
        self.bKashURL="https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/"
        self.createURL="https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/create"


    def live(self):
        self.bKashURL="https://tokenized.bka.sh/v1.2.0-beta/tokenized/checkout/"
       


ci = CredentialInfo()


def credential(app_key,app_secret,bKashUsername,bKashPassword):
    ci.setCredendial(app_key,app_secret,bKashUsername,bKashPassword)


def useSandBoxURLs():
    ci.sandbox()


def useLiveURLs():
    ci.live()


def createURL(url):
    ci.createURL=url


def grant():
    url = ci.bKashURL + "token/grant"


    payload = {
        "app_key": ci.app_key,
        "app_secret": ci.app_secret
    }
    headers = {
        "accept": "application/json",
        "username": ci.bKashUsername,
        "password": ci.bKashPassword,
        "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    ci.authorization = response.json()['id_token']
    return response.json()




def createpayment(callbackURL,amount, intent, merchantInvoiceNumber, payerReference):
    url = ci.createURL
   
    payload = {
        "mode": "0011",
        "callbackURL": callbackURL,
        "amount": amount,
        "currency": "BDT",
        "intent": intent,
        "merchantInvoiceNumber": merchantInvoiceNumber,
        "payerReference": payerReference
    }
    headers = {
        "accept": "application/json",
        "Authorization": ci.authorization,
        "X-APP-Key": ci.app_key,
        "content-type": "application/json"
    }
   
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def execute(paymentID):
   
    url = ci.bKashURL + "execute"


    payload = {"paymentID": paymentID}
   
    headers = {
        "accept": "application/json",
        "Authorization": ci.authorization,
        "X-APP-Key": ci.app_key,
        "content-type": "application/json"
    }
   
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def refund(trxID,amount,reason,sku):
    url = ci.bKashURL + "refund"
   
    paymentID=searchTransaction(trxID)['paymentID']


    payload = {
      "paymentID": paymentID,
      "trxID": trxID,
      "amount": amount,
      "sku": sku,
      "reason": reason
}


    headers = {
        "accept": "application/json",
        "Authorization": ci.authorization,
        "X-APP-Key": ci.app_key,
        "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def searchTransaction(trxID):
    grant()


    url = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/general/searchTransaction"


    payload = trxID
    headers = {
        "accept": "application/json",
        "Authorization": ci.authorization,
        "X-APP-Key": ci.app_key,
        "content-type": "application/json"
    }


    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def createAgreement(callbackURL,amount, intent, merchantInvoiceNumber, payerReference):
    url = ci.createURL
    payload = {
        "mode": "0000",
        "callbackURL": callbackURL,
        "amount": amount,
        "currency": "BDT",
        "intent": intent,
        "merchantInvoiceNumber": merchantInvoiceNumber,
        "payerReference": payerReference
    }
    headers = {
        "accept": "application/json",
        "Authorization": ci.authorization,
        "X-APP-Key": ci.app_key,
        "content-type": "application/json"
    }
   
    response = requests.post(url, json=payload, headers=headers)
    return response.json()




def createAgreement_payment(agreementID,callbackURL,amount,
                            intent, merchantInvoiceNumber, payerReference):
    url = ci.createURL
   
    payload = {
        'agreementID': agreementID,
        "mode": "0001",
        "callbackURL": callbackURL,
        "amount": amount,
        "currency": "BDT",
        "intent": intent,
        "merchantInvoiceNumber": merchantInvoiceNumber,
        "payerReference": payerReference
    }
    headers = {
        "accept": "application/json",
        "Authorization": ci.authorization,
        "X-APP-Key": ci.app_key,
        "content-type": "application/json"
    }
   
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def paymentStatus(paymentID):
    grant()


    url = ci.bKashURL + "payment/status"


    payload = {"paymentID": paymentID}
    headers = {
        "accept": "application/json",
        "Authorization": ci.authorization,
        "X-APP-Key": ci.app_key,
        "content-type": "application/json"
    }


    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def query(paymentID):
    return paymentStatus(paymentID)
