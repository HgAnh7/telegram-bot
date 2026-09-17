from aiogram import Router

from .start import router as start_router
from .help import router as help_router
from .nct import router as nct_search


router = Router()

router.include_router(start_router)
router.include_router(help_router)
router.include_router(nct_search)