def custom500(error):
    return type(error)

handler = {
    500: custom500,
}
