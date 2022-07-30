project( blue )
cmake_minimum_required( VERSION 2.6 )
install( FILES "${CMAKE_CURRENT_SOURCE_DIR}/blue.py" DESTINATION "/lib/python3/dist-packages/blue" )
add_custom_command(TARGET blue
    # Run after all other rules within the target have been executed
    POST_BUILD
    COMMAND pip3 install wxpython
    COMMENT ""
    VERBATIM
)
