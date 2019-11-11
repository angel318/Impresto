def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.ai', '.cdr', '.doc', '.docx', '.dwg', '.dxf', '.eps', '.jpeg', '.jpg', '.pdf', '.plt', '.png', '.psd', '.txt', '.xls', 'xlsx', 'zip', 'rar']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Tipo de archivo no soportado.')
