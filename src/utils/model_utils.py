"""Module provides utility functions for model manipulations"""


def get_field_names(model: "BaseModel") -> List[str]:
    """
    Extracts field names from given model.

    Example:
        class User(BaseModel):
             username: str
             password: str

             @computed_field
             @property
             def full_name(self) -> str:
                 return self.username


        get_field_names(User)
        ['username', 'password', 'full_name']

    Args:
        model (BaseModel) -- model to extract fields from.
        Could be any class inherited from pydantic BaseModel

    Returns:
        List[str] -- list of field names
    """
    fields = list(model.model_fields.keys())
    fields.extend(list(model.model_computed_fields.keys()))
    return fields
