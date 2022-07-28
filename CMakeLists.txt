project( blue )
cmake_minimum_required( VERSION 2.6 )
file( GLOB hcnc_py "${CMAKE_CURRENT_SOURCE_DIR}/*.py" "${CMAKE_CURRENT_SOURCE_DIR}/pycnc/*.py")
list( REMOVE_ITEM hcnc_py
  "${CMAKE_CURRENT_SOURCE_DIR}/post.py"
  "${CMAKE_CURRENT_SOURCE_DIR}/POST_TEST.py"
  "${CMAKE_CURRENT_SOURCE_DIR}/STLTools.py"
)
install( FILES "${CMAKE_CURRENT_SOURCE_DIR}/*.py" DESTINATION ${LIB_INSTALL_DIR}/blue )