Pip install bkashpgw

Modules:
 Tokenized Checkout URL with Refund 
 Agreemented Tokenized Checkout URL with Refund 

import bkashpgw as bKash

useSandBoxURLs()           to use urls of sandbox credentials
useLiveURLs()                     to use urls of live credentials
 Tokenized Checkout URL with Refund 
Set the credentials provided by bKash
Set your website baseURL
Create payment and redirect to bKashURL
Execute the payment in the callbackURL function if create is successful
If no response from execute, call query



uses
functions
returns
1
Set the credential
bKash.credential(“username”,“password”,“app_key”,“app_secret”)
-
2
Set the baseURL
bKash.baseurl(“http://127.0.0.1:8000/”)
-
3
Set the bKash URL for create
bKash.setURLS(“https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/”,)
-
6
Create the payment
 Save the paymentID from response, redirect to bKashUrl
bKash.createpayment(callbackURL,amount, intent, merchantInvoiceNumber, payerReference)
[bkashUrl,paymentID,response.json() as dict]
7
Execute in the callbackURL function
  Save the trxID from response
bKash.execute(paymentID)


8
Refund for a payment
bKash.refund(trxID,amount,reason)
response.json() as dict
9
Check refund status
bKash.refundCheck(trxID)


10
To call query 
bKash.query(paymentID)


11
To search a transaction
bKash.searchTransaction(trxID)


12
check payment status
bKash.paymentStatus(paymentID)


13
To grant authorization token
bKash.grant()
[authorization token, response.jon()  as dict]




Agreemented Tokenized Checkout URL with Refund 
Set the credentials provided by bKash
Set your website baseURL
Check if the user  wants to pay through agreement and if he has agreementID
If he has agreementID proceed to Step 6 then 7
If the user wants to create a new agreementID with new number, proceed from Step 4 to 7
If someone wants to cancel the agreement, call the cancelAgree and delete the agreementID and phone number from the user's info.


uses
functions


1
Set the credential
bKash.credential(“username”,“password”,“app_key”,“app_secret”)


2
Set the baseURL
bKash.baseurl(“http://127.0.0.1:8000/”)


3
Set the bKash URL
bKash.setURLS(“https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/token/grant”,”https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/”,)


4
Create the agreement for agreement pgw
 Save the paymentID from response
bKash.createAgreement(callbackURL,amount, intent, merchantInvoiceNumber, payerReference) 
bKash.createAgreement(callbackURL)


5
Execute in the callbackURL function
  Save the agreementID and customerMsisdn from response
bKash.execute(request.GET['paymentID'])


6
Create the payment for agreement
 Save the paymentID from response
bKash.createAgreement_payment(agreementID,callbackURL,amount, intent, merchantInvoiceNumber, payerReference)


7
Execute in the callbackURL function
  Save the trxID from response
bKash.execute(request.GET['paymentID'])


8
Cancel Agreement
bKash.cancelAgree(agreementID)


9
Refund for a payment
bKash.refund(trxID,amount,reason)
response.json() as dict
10
Check refund status
bKash.refundCheck(trxID)


11
To call query and check payment status
bKash.query(paymentID)


12
To search a transaction
bKash.searchTransaction(trxID)


13
To grant authorization token
bKash.grant()
[authorization token, response.jon()  as dict]



