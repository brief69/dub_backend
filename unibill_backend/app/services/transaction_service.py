

# app/services/transaction_service.py

# loggingモジュールをインポートしてログ情報を表示できるように設定します。
import logging
# INFOレベル以上のログが表示されるよう設定します。
logging.basicConfig(level=logging.INFO)

# TransactionHistoryServiceクラスを定義します。
class TransactionHistoryService:

    # インスタンスが生成される際に呼び出される特殊メソッドです。
    def __init__(self):
        # ユーザーデータを保持する辞書を初期化します。キーはuser_id、値はusefulnessです。
        self.user_data = {}

    # ユーザーデータを更新するメソッドです。
    def update_user_data(self, user_id, success):
        """Update the user data based on transaction result."""
        # 指定されたuser_idがuser_data辞書に存在しない場合、新たにキーとして追加し、値を0に設定します。
        if user_id not in self.user_data:
            self.user_data[user_id] = 0
        
        # 引数successがTrue（取引成功）で、かつuser_dataの値が100未満の場合、user_dataの値を1増加させます。
        if success and self.user_data[user_id] < 100:
            self.user_data[user_id] += 1
        # successがFalse（取引失敗）の場合、user_dataの値を10減少させます。ただし、0未満にはならないよう調整します。
        elif not success:
            self.user_data[user_id] = max(0, self.user_data[user_id] - 10)

        # ログにuser_idと更新後のusefulnessを出力します。
        logging.info(f"Updated user {user_id}. Usefulness: {self.user_data[user_id]}")
