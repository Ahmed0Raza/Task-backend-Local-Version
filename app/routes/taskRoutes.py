from fastapi import APIRouter, Depends, Request
from app.controllers.taskControllers import createTask, updateTask, deleteTask, fetchTask
from app.middleware.auth import verify_token

router = APIRouter()

# Apply verify_token only to protected routes
router.post("/createTask", dependencies=[Depends(verify_token)])(createTask)
router.put("/updateTask/{task_id}", dependencies=[Depends(verify_token)])(updateTask)
router.delete("/deleteTask/{task_id}", dependencies=[Depends(verify_token)])(deleteTask)
router.get("/fetchTask/{task_id}", dependencies=[Depends(verify_token)])(fetchTask)
