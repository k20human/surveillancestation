errors = {
    # Common error codes of wrong parameters or failed login for all WebAPIs
    100: 'Unknown error',
    101: 'No parameter of API, method or version',
    102: 'The requested API does not exist',
    103: 'The requested method does not exist',
    104: 'The requested version does not support the functionality',
    105: 'The logged in session does not have permission',
    106: 'Session timeout',
    107: 'Session interrupted by duplicate login',
    400: 'Execution failed',
    401: 'Parameter invalid',
    402: 'Camera disabled',
    407: 'CMS closed',
    500: 'Server error',

    'SYNO.API.Auth': {
        101: 'The account parameter is not specified',
        400: 'Invalid password',
        401: 'Guest or disabled account',
        402: 'Permission denied',
        403: 'One time password not specified',
        404: 'One time password authenticate failed'
    }
}
