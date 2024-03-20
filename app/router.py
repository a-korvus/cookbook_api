"""Routes in this app."""

from fastapi import APIRouter, Path, HTTPException, status
from typing import Annotated

from .models import Recipe
from .queries import get_all_recipes, get_recipe_by_id
from .schemas import RecipeSchema, RecipeSchemaDeatil, NotFoundMessage

router = APIRouter(
    prefix="/cookbook/api",
    tags=["cookbook"]
)


@router.get("/recipes",)
async def all_recipes() -> list[RecipeSchema]:
    """Get the list of recipes."""
    result: list[Recipe] = await get_all_recipes()

    return result


@router.get(
    path="/recipes/{recipe_id}",
    responses={404: {"model": NotFoundMessage}},
)
async def recipe(
    recipe_id: Annotated[
        int, Path(
        title="Recipe ID",
        description="Your recipe ID, please",
        ),
    ],
) -> RecipeSchemaDeatil:
    """Get all data of recipe."""
    recipe: Recipe = await get_recipe_by_id(recipe_id)
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    recipe = RecipeSchemaDeatil.model_validate(recipe)
    return recipe
