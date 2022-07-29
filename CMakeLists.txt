project( blue )
cmake_minimum_required( VERSION 2.6 )
find_package(Python)
message(STATUS "PYTHON_DEFAULT_EXECUTABLE = " ${PYTHON_DEFAULT_EXECUTABLE})
message(STATUS "PYTHON3_EXECUTABLE = ${PYTHON3_EXECUTABLE}")
execute_process(
  COMMAND "${PYTHON_EXECUTABLE}" -c "if True:
    from distutils import sysconfig as sc
    print(sc.get_python_lib(prefix='', plat_specific=True))"
  OUTPUT_VARIABLE PYTHON_SITE
  OUTPUT_STRIP_TRAILING_WHITESPACE)
message(STATUS "PYTHON_SITE = ${PYTHON_SITE}")
install( FILES "${CMAKE_CURRENT_SOURCE_DIR}/blue.py" DESTINATION ${PYTHON_SITE}/blue )
