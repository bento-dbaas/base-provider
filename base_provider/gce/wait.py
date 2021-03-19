from base_provider.base import BaseProvider


class Wait(BaseProvider):

    client = None
    credential = None

    def __init__(self):
        pass

    def wait_zone_operation(self, zone, operation):
        op = self.client.zoneOperations().wait(
            project=self.credential.project,
            zone=zone,
            operation=operation
        ).execute()
        return self._check_operation_status(op)

    def wait_global_operation(self):
        pass

    def _check_operation_status(self, operation):
        if operation.get('error'):
            error = 'Error in {} operation: {}'.format(
                operation.get('operationType'),
                operation.get('error')
            )
            raise Exception(error)

        if operation.get('status') != 'DONE':
            error = 'Operation {} is not Done. Status: {}'.format(
                operation.get('operationType'),
                operation.get('status')
            )
            raise Exception(error)

        return True
