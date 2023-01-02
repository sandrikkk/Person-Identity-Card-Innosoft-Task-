from rest_framework import serializers
from person.models import Person, Characteristics

class CharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields = ['id', 'characteristics']

class PersonSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicsSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ['id','name', 'last_name', 'photo', 'cardnum', 'city', 'sex', 'personalid', 'department', 'characteristics', 'dateofbirth', 'dateofexpiry']
