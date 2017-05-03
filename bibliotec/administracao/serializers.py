from rest_framework import serializers
from .models import Livro, Cliente, Reserva


class LivroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livro
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'


class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = ('cliente', 'livro', 'data_reserva')















   # cliente = serializers.HyperlinkedRelatedField(
   #      many=False,
   #      read_only=True,
   #      view_name='cliente_detail'
   #  )