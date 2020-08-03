from marshmallow import Schema, fields, validate


class CategorySchema(Schema):
    id = fields.Integer()
    name = fields.String(validate=validate.Length(min=1, max=30), required=True)
    description = fields.String(validate=validate.Length(min=1, max=200), required=True)
    image_url = fields.Url(validate=validate.Length(max=200), required=True)
