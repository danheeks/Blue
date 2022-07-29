project( blue )
cmake_minimum_required( VERSION 2.6 )
FIND_PACKAGE(python)
execute_process(
  COMMAND "${PYTHON_EXECUTABLE}" -c "if True:
    from distutils import sysconfig as sc
    print(sc.get_python_lib(prefix='', plat_specific=True))"
  OUTPUT_VARIABLE PYTHON_SITE
  OUTPUT_STRIP_TRAILING_WHITESPACE)
message(STATUS "PYTHON_EXECUTABLE = ${PYTHON_EXECUTABLE}")
message(STATUS "PYTHON_SITE = ${PYTHON_SITE}")
install( FILES "${CMAKE_CURRENT_SOURCE_DIR}/blue.py" DESTINATION ${PYTHON_SITE}/blue )
