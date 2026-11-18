from rest_framework import mixins, generics


class ProMixinsGenricsAPI(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    pass

class ProMixinsDetailGenricsAPI(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    pass