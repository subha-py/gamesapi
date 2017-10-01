Understanding: 
1) Options in restapi:
    We have to support for "options" option against http request.
    Option is a general command we use to query to get allowed methos for that api.
    Example: in function based views if we only allow request.method in views it will give error for other options and break our server.
    So to avoid that we have to use decorators.
2) Content type in rest api:
    We also have to support different return types in rest api only application/json return in bad design.

3) Using api_view decorator:
    actually makes a subclass of rest_framework.views.APIView and it handles many thing like
    
    a. It responds with proper status code to unsupported request verbs.
    
    b. If request.data is used and parsers are not able to parse, then it will respond with proper status code.
    
    c. default parsers are jsonparser(application/json), formdata_parser(application/x-www-form-urlencoded), MultiPartParser(multipart/formdata).
    
    d. default renderers are JSON renderer(application/json) and Browsableapirenderer(text/html).
    
    e. DEFAULT_CONTENT_NEGOTATION_CLASS is the restframework.negotiation.DefaultContentNegotiation class.
    This class helps to judge the request "accept" attribute and use proper renderers.
    
    f. csrf_exempt is also added
    
4) For request type form(application/x-www-form-urlencoded):
    The request.data is passed to rest_framework.parsers.FormParser before going to serializer.
    
5) The browsable api will work after api_view decorator is added to a function, since it will
    add the accept type text/html response after that.
    
6) Put vs Patch: Put means rewriting an existing row. Patch means updating one attribute of a row.
7) In serializers, the fields form modelserializers you don't want to include in post method, make them read_only=true.
8) throttling - if we want to group a number of view classes to server with a rate. We can do so by using throttle_scope 
variable and sopedratethrottle, this will override the default and use the scope defined in throttle_scope
used, which is again specified in settngs.py