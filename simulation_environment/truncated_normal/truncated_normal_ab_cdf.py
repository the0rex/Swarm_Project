#! /usr/bin/env python
#
def truncated_normal_ab_cdf ( x, mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_CDF evaluates the Truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real VALUE, the value of the CDF.
# 
  from normal_01_cdf import normal_01_cdf

  if ( x < a ):
  
    value = 0.0
    
  elif ( x <= b ):
  
    alpha = ( a - mu ) / sigma
    beta = ( b - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = normal_01_cdf ( alpha )
    beta_cdf = normal_01_cdf ( beta )
    xi_cdf = normal_01_cdf ( xi )

    value = ( xi_cdf - alpha_cdf ) / ( beta_cdf - alpha_cdf )
    
  else:
  
    value = 1.0

  return value

def truncated_normal_ab_cdf_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_CDF_TEST tests TRUNCATED_NORMAL_AB_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from truncated_normal_ab_cdf_values import truncated_normal_ab_cdf_values

  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_CDF evaluates the CDF' )
  print ( '  of the Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean = mu' )
  print ( '    standard deviation = sigma' )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [a,b]' )

  print ( '' )
  print ( '                                                           Stored         Computed' )
  print ( '       X        Mu         S         A         B             CDF             CDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, b, x, cdf1 = truncated_normal_ab_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    cdf2 = truncated_normal_ab_cdf ( x, mu, sigma, a, b )

    print ( '  %8.1f  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, a, b, cdf1, cdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_CDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_ab_cdf_test ( )
  timestamp ( )


