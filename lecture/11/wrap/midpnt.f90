! FILE: midpnt.f90
  subroutine midpnt(func,lowerLimit,upperLimit,integral,refinementStage)
    integer, intent(in)           :: refinementStage
    real*8 , intent(in)           :: lowerLimit,upperLimit
    real*8 , intent(out)          :: integral
    !real*8 , external             :: func
    integer                       :: it,j
    
    interface
      real*8 function func(x)
        real*8, intent(in) :: x
      end function func
    end interface
    
    real*8 ddel,del,summ,tnm,x
    if (refinementStage==1) then
      integral = (upperLimit-lowerLimit) * func( 0.5d0 * (lowerLimit+upperLimit) )
    else
      it = 3**(refinementStage-2)
      tnm = it
      del = (upperLimit-lowerLimit) / (3.0d0*tnm)
      ddel = del+del
      x = lowerLimit + 0.5d0*del
      summ = 0.0d0
      do j = 1,it
        summ = summ + func(x)
        x = x + ddel
        summ = summ + func(x)
        x = x + del
      end do
      integral = ( integral + (upperLimit-lowerLimit)*summ/tnm ) / 3.0d0
    endif
  end subroutine midpnt
! END FILE: midpnt.f90