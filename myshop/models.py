from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  isActive = models.BooleanField(default=True)

  def __str__(self):
    return self.name

class Business(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  shopName = models.CharField(max_length=200, null=True, blank=True)
  phoneNumber = models.CharField(max_length=100, null=True, blank=True)
  image = models.ImageField(null=True, blank=True)
  isActive = models.BooleanField(default=True)
  updatedAt = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Product(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  image = models.ImageField(null=True, blank=True)
  brand = models.CharField(max_length=200, null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  description = models.TextField(null=True, blank=True)
  rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  numReviews = models.IntegerField(null=True, blank=True, default=0)
  price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  countInStock = models.IntegerField(null=True, blank=True, default=0)
  updatedAt = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return self.name

class Review(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  rating = models.IntegerField(null=True, blank=True, default=0)
  comment = models.TextField(null=True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.rating)

class VoucherSettings(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.name)

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  paymentMethod = models.CharField(max_length=200, null=True, blank=True)
  taxPrice = models.DecimalField(
    max_digits=7, decimal_places=2, null=True, blank=True)
  shippingPrice = models.DecimalField(
    max_digits=7, decimal_places=2, null=True, blank=True)
  totalPrice = models.DecimalField(
    max_digits=7, decimal_places=2, null=True, blank=True)
  isPaid = models.BooleanField(default=False)
  paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
  isDelivered = models.BooleanField(default=False)
  deliveredAt = models.DateTimeField(
    auto_now_add=False, null=True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    return str(self.createdAt)

class Voucher(models.Model):
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  voucherSettings = models.ForeignKey(VoucherSettings, on_delete=models.SET_NULL, null=True)
  voucherKey = models.CharField(max_length=200, null=True, blank=True)
  recipientPhone = models.CharField(max_length=200, null=True, blank=True)
  recipientEmail = models.CharField(max_length=200, null=True, blank=True)
  transactionDate = models.CharField(max_length=200, null=True, blank=True)
  deliveredAmount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  requestedAmount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  operatorName = models.CharField(max_length=200, null=True, blank=True)
  transactionId = models.CharField(max_length=300, null=True, blank=True)
  operatorTransactionId = models.CharField(max_length=200, null=True, blank=True)
  countryCode = models.CharField(max_length=200, null=True, blank=True)
  isActive = models.BooleanField(default=True)
  updatedAt = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __int__(self):
    return int(self.order)

class Payment(models.Model):
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  tx_ref = models.CharField(max_length=200, null=True, blank=True)
  flw_ref = models.CharField(max_length=200, null=True, blank=True)
  amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  currency = models.CharField(max_length=200, null=True, blank=True)
  charged_amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  app_fee = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  merchant_fee = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  processor_response = models.CharField(max_length=200, null=True, blank=True)
  ip = models.CharField(max_length=200, null=True, blank=True)
  narration = models.TextField(null=True, blank=True)
  status = models.CharField(max_length=200, null=True, blank=True)
  payment_type = models.CharField(max_length=200, null=True, blank=True)
  payed_at = models.CharField(max_length=200, null=True, blank=True)
  account_id = models.CharField(max_length=100, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)
  updatedAt = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(auto_now_add=True)

  def __int__(self):
    return int(self.order)


class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  qty = models.IntegerField(null=True, blank=True, default=0)
  price = models.DecimalField(
    max_digits=7, decimal_places=2, null=True, blank=True)
  image = models.CharField(max_length=200, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)
  createdAt = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.name)

class ShippingAddress(models.Model):
  order = models.OneToOneField(
    Order, on_delete=models.CASCADE, null=True, blank=True)
  address = models.CharField(max_length=200, null=True, blank=True)
  city = models.CharField(max_length=200, null=True, blank=True)
  postalCode = models.CharField(max_length=200, null=True, blank=True)
  country = models.CharField(max_length=200, null=True, blank=True)
  shippingPrice = models.DecimalField(
    max_digits=7, decimal_places=2, null=True, blank=True)
  _id = models.AutoField(primary_key=True, editable=False)
  updatedAt = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.address)