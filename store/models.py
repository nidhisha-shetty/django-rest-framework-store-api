from django.db import models
# Create your models here.

class Store(models.Model):
	company_name=models.CharField(max_length=50)
	company_gst_no=models.CharField(max_length=200)
	def __str__(self):
		return self.company_name

class Product(models.Model):
	company_name=models.ForeignKey(Store, on_delete=models.CASCADE)
	product_name=models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.product_name

class Purchase(models.Model):
	company_name=models.ForeignKey(Store, on_delete=models.CASCADE)
	product_name=models.ForeignKey(Product, on_delete=models.CASCADE)
	purchase_rate=models.IntegerField(null=False)
	purchase_quantity=models.IntegerField(null=False)



