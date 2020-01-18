"""
This combines the different graphql schemas into a single endpoint for flask to serve.
The schema needs to be imported in order to be used.
"""
import graphene

import app.auth.schema as auth_schema
import app.main.schema as main_schema


class Query(auth_schema.Query, main_schema.Query, graphene.ObjectType):
    pass


class Mutation(auth_schema.Mutation, main_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
