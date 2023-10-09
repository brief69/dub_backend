

# app/api/transaction_api.py

# TransactionHistoryServiceクラスをimportします。
from app.services.transaction_service import TransactionHistoryService

# TransactionAPIクラスを定義します。
class TransactionAPI:

    # コンストラクタでTransactionHistoryServiceのインスタンスを受け取り、内部に保持します。
    def __init__(self, history_service):
        self.history_service = history_service
    
    # notify_transactionメソッドを定義します。これは外部から取引結果の通知を受け取り、
    # TransactionHistoryServiceを用いてユーザーデータを更新します。
    def notify_transaction(self, user_id, success):
        """Receive transaction notification and update the user data."""
        # TransactionHistoryServiceのupdate_user_dataメソッドを呼び出してユーザーデータを更新します。
        self.history_service.update_user_data(user_id, success)

# Usage Example
# TransactionHistoryServiceのインスタンスを生成します。
history_service = TransactionHistoryService()
# TransactionAPIのインスタンスを生成し、先ほど生成したhistory_serviceを引数として渡します。
api = TransactionAPI(history_service)

# TransactionAPIのnotify_transactionメソッドを呼び出し、取引結果の通知を模擬します。
# 下記の例では、"user1"に対して、2回取引成功の通知と1回取引失敗の通知を行います。
api.notify_transaction("user1", True)  # "user1"の取引が成功したことを通知。
api.notify_transaction("user1", True)  # "user1"の取引が再度成功したことを通知。
api.notify_transaction("user1", False) # "user1"の取引が失敗したことを通知。
