import csv
import io
from typing import List

from orders.models import Order


class SalesReport:

    def get_querysets(self):
        orders = Order.objects.filter(is_active=False).order_by('order_date')
        return [orders]

    def get_headers(self):
        return ['Order id', 'Customer', 'Email', 'Product', 'Quantity', 'Price', 'Total price', 'Order date']

    def prepare_data(self, orders):
        product_data = []
        if orders:
            for order in orders:
                for item in order.items.all():
                    product_data.append(
                        [
                            order.id,
                            order.user.username,
                            order.user.email,
                            item.product.name,
                            item.quantity,
                            item.product.price,
                            order.total_price,
                            order.order_date.strftime("%d-%m-%Y")
                        ]
                    )
                product_data.append(['' * len(self.get_headers())])

        return product_data

    def create_report(self, headers: List[str], data: list):
        buffer = io.StringIO()
        wr = csv.writer(buffer)
        # set headers
        wr.writerow(headers)
        if data:
            # insert rows
            wr.writerows(data)
        buffer.seek(0)
        return buffer

    def result(self):
        querysets = self.get_querysets()
        data = self.prepare_data(*querysets)
        return self.create_report(self.get_headers(), data)
