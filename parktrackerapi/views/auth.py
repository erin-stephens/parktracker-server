from rest_framework.decorators import api_view
from rest_framework.response import Response
from parktrackerapi.models import User


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    user = User.objects.filter(uid=uid).first()

    if user is not None:
        data = {
            'id': user.id,
            'uid': user.uid,
            'bio': user.bio,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    user = User.objects.create(
        bio=request.data['bio'],
        uid=request.data['uid'],
        first_name=request.data['firstName'],
        last_name=request.data['lastName']
    )

    data = {
            'id': user.id,
            'uid': user.uid,
            'bio': user.bio,
            'first_name': user.first_name,
            'last_name': user.last_name
    }
    return Response(data)
