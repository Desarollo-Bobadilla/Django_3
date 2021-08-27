from ..models import Variable

def get_all_variables():
    return Variable.objects.all()