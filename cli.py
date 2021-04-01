"""'Moore.io Core CLI'.

Usage:
  # Digital Logic Simulation
  mio clean [<target>] [-a | --all] [-w | --wipe_results]
  mio lib    <target>  [-nr | --non_recursive]
  mio sim    <target>  [-t <test_name>]  [-s <seed>]  [-g | --gui]  [-w | --waves]
  mio cmp    <target>
  mio elab   <target>  [-d | --debug]
  mio cpel   <target>  [-d | --debug]
  mio oss    <target>  [-t <test_name>]  [-s <seed>]  [-g | --gui]  [-d | --debug]  [-w | --waves]  [-q | --noclean]
  mio rrg    <test_suite>  <regression_name>
  
  # Generators & Refactoring & Documentation Generator -- Cool mio exclusives!
  mio new      [<generator_name>]
  mio refactor <target>  (disconnect|connect|rename|delete)
  mio docgen [target_ip]  [-a | --all]
  
  # Misc. EDA
  mio lint # tbd
  mio synt # tbd
  
  mio doctor
  mio (-h | --help)
  mio --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""


"""'Moore.io IP Manager CLI'.

Usage:
  mpm init
  mpm config
  
  mpm search
  mpm install
  mpm uninstall
  mpm list
  mpm prune
  mpm outdated
  mpm update
  
  mpm login
  mpm logout
  
  mpm publish
  mpm unpublish
  mpm deprecate
  mpm shrinkwrap
  
  mio doctor
  mio (-h | --help)
  mio --version
  
Options:
  -h --help     Show this screen.
  --version     Show version.

"""