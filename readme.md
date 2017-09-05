Understanding: 
1) Options in restapi:
    We have to support for "options" option against http request.
    Option is a general command we use to query to get allowed methos for that api.
    Example: in function based views if we only allow request.method in views it will give error for other options and break our server.
    So to avoid that we have to use decorators.
2) Content type in rest api:
    We also have to support different return types in rest api only application/json return in bad design.