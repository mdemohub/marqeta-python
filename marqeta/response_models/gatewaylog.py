from datetime import datetime
from marqeta.response_models.gatewaylog import Gatewaylog


class Gatewaylog(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def id(self):
        if 'id' in self.json_response:
            return self.json_response['id']

    @property
    def traceNumber(self):
        if 'traceNumber' in self.json_response:
            return self.json_response['traceNumber']

    @property
    def paymentTypeCode(self):
        if 'paymentTypeCode' in self.json_response:
            return self.json_response['paymentTypeCode']

    @property
    def achTransactionType(self):
        if 'achTransactionType' in self.json_response:
            return self.json_response['achTransactionType']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    @property
    def gatewayVersion(self):
        if 'gatewayVersion' in self.json_response:
            return self.json_response['gatewayVersion']

    @property
    def gatewayResponse(self):
        if 'gatewayResponse' in self.json_response:
            return self.json_response['gatewayResponse']

    @property
    def timedOut(self):
        if 'timedOut' in self.json_response:
            return self.json_response['timedOut']

    @property
    def deal_Id(self):
        if 'deal_Id' in self.json_response:
            return self.json_response['deal_Id']

    @property
    def order_Id(self):
        if 'order_Id' in self.json_response:
            return self.json_response['order_Id']

    @property
    def request_method(self):
        if 'request_method' in self.json_response:
            return self.json_response['request_method']

    @property
    def response_code(self):
        if 'response_code' in self.json_response:
            return self.json_response['response_code']

    @property
    def response_subcode(self):
        if 'response_subcode' in self.json_response:
            return self.json_response['response_subcode']

    @property
    def response_reasoncode(self):
        if 'response_reasoncode' in self.json_response:
            return self.json_response['response_reasoncode']

    @property
    def response_message(self):
        if 'response_message' in self.json_response:
            return self.json_response['response_message']

    @property
    def status(self):
        if 'status' in self.json_response:
            return self.json_response['status']

    @property
    def fraud_avs(self):
        if 'fraud_avs' in self.json_response:
            return self.json_response['fraud_avs']

    @property
    def fraud_auth(self):
        if 'fraud_auth' in self.json_response:
            return self.json_response['fraud_auth']

    @property
    def fraud_cvv(self):
        if 'fraud_cvv' in self.json_response:
            return self.json_response['fraud_cvv']

    @property
    def gateway_transactionId(self):
        if 'gateway_transactionId' in self.json_response:
            return self.json_response['gateway_transactionId']

    @property
    def original_gateway(self):
        if 'original_gateway' in self.json_response:
            return Gatewaylog(self.json_response['original_gateway'])

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def duplicate(self):
        if 'duplicate' in self.json_response:
            return self.json_response['duplicate']

    @property
    def post_date(self):
        if 'post_date' in self.json_response:
            return datetime.strptime(self.json_response['post_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def response_time(self):
        if 'response_time' in self.json_response:
            return datetime.strptime(self.json_response['response_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def api_duration(self):
        if 'api_duration' in self.json_response:
            return self.json_response['api_duration']

    @property
    def gateway_duration(self):
        if 'gateway_duration' in self.json_response:
            return self.json_response['gateway_duration']

    @property
    def ach_status(self):
        if 'ach_status' in self.json_response:
            return self.json_response['ach_status']

    @property
    def created(self):
        if 'created' in self.json_response:
            return datetime.strptime(self.json_response['created'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def modified(self):
        if 'modified' in self.json_response:
            return datetime.strptime(self.json_response['modified'], '%Y-%m-%dT%H:%M:%SZ')

