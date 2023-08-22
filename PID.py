
#*****************************************************************#
#                       Incremental PID system                    #            
#*****************************************************************#
class IncrementalPID:
    #Inițializează valorile celor trei constante (P, I și D) care determină intensitatea termenilor proporțional
    def __init__(self, P, I, D):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        #Iesirea PID curenta
        self.PIDOutput = 0.0    
        #iesirea curenta a sistemului
        self.SystemOutput = 0.0    
        #iesirea anterioara a sistemului
        self.LastSystemOutput = 0.0    
 
        #cele 3 erori
        self.Error = 0.0              
        self.LastError = 0.0
        self.LastLastError = 0.0
 
    #Seteaza iesirea dorita a sistemului
    def SetStepSignal(self,StepSignal):
        self.Error = StepSignal - self.SystemOutput
        IncrementValue = self.Kp * (self.Error - self.LastError) +\
        self.Ki * self.Error +\
        self.Kd * (self.Error - 2 * self.LastError + self.LastLastError)

        self.PIDOutput += IncrementValue
        self.LastLastError = self.LastError
        self.LastError = self.Error

    #Seteaza iesirea curenta a sistemului pe baza inertiei sistemului
    def SetInertiaTime(self,InertiaTime,SampleTime):
        self.SystemOutput = (InertiaTime * self.LastSystemOutput + \
            SampleTime * self.PIDOutput) / (SampleTime + InertiaTime)

        self.LastSystemOutput = self.SystemOutput
 
 
# *****************************************************************#
#                      Positional PID system                      #
# *****************************************************************#
class PositionalPID:
    def __init__(self, P, I, D):
        self.Kp = P
        self.Ki = I
        self.Kd = D
 
        self.SystemOutput = 0.0
        self.ResultValueBack = 0.0
        self.PidOutput = 0.0
        self.PIDErrADD = 0.0
        self.ErrBack = 0.0
    

    def SetStepSignal(self,StepSignal):
        Error = StepSignal - self.SystemOutput
        Kp = self.Kp * Error
        Ki = self.Ki * self.PIDErrADD
        Kd = self.Kd * (Error - self.ErrBack)
        self.PidOutput = Kp + Ki + Kd
        self.PIDErrADD += Error
        if self.PIDErrADD > 2000:
            self.PIDErrADD = 2000
        if self.PIDErrADD < -2500:
            self.PIDErrADD = -2500
        self.ErrBack = Error
        

    def SetInertiaTime(self, InertiaTime,SampleTime):
           self.SystemOutput = (InertiaTime * self.ResultValueBack + \
           SampleTime * self.PidOutput) / (SampleTime + InertiaTime)

           self.ResultValueBack = self.SystemOutput
       