from callapp.models import Call
from rest_framework import serializers

class CallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Call
        fields = ('id', 'type', 'timestampstart', 'timestampend', 'call_id', 'source', 'destination')

