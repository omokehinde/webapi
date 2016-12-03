from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

	class Meta:
		model = Stock
		# fields = ('ticker', 'volume') it will return just ticker and volume
		fields = '__all__' # it will return all