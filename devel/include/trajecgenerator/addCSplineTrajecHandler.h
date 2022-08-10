// Generated by gencpp from file trajecgenerator/addCSplineTrajecHandler.msg
// DO NOT EDIT!


#ifndef TRAJECGENERATOR_MESSAGE_ADDCSPLINETRAJECHANDLER_H
#define TRAJECGENERATOR_MESSAGE_ADDCSPLINETRAJECHANDLER_H

#include <ros/service_traits.h>


#include <trajecgenerator/addCSplineTrajecHandlerRequest.h>
#include <trajecgenerator/addCSplineTrajecHandlerResponse.h>


namespace trajecgenerator
{

struct addCSplineTrajecHandler
{

typedef addCSplineTrajecHandlerRequest Request;
typedef addCSplineTrajecHandlerResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct addCSplineTrajecHandler
} // namespace trajecgenerator


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::trajecgenerator::addCSplineTrajecHandler > {
  static const char* value()
  {
    return "b8d56f785274552c60142c0b2c2c3c51";
  }

  static const char* value(const ::trajecgenerator::addCSplineTrajecHandler&) { return value(); }
};

template<>
struct DataType< ::trajecgenerator::addCSplineTrajecHandler > {
  static const char* value()
  {
    return "trajecgenerator/addCSplineTrajecHandler";
  }

  static const char* value(const ::trajecgenerator::addCSplineTrajecHandler&) { return value(); }
};


// service_traits::MD5Sum< ::trajecgenerator::addCSplineTrajecHandlerRequest> should match
// service_traits::MD5Sum< ::trajecgenerator::addCSplineTrajecHandler >
template<>
struct MD5Sum< ::trajecgenerator::addCSplineTrajecHandlerRequest>
{
  static const char* value()
  {
    return MD5Sum< ::trajecgenerator::addCSplineTrajecHandler >::value();
  }
  static const char* value(const ::trajecgenerator::addCSplineTrajecHandlerRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::trajecgenerator::addCSplineTrajecHandlerRequest> should match
// service_traits::DataType< ::trajecgenerator::addCSplineTrajecHandler >
template<>
struct DataType< ::trajecgenerator::addCSplineTrajecHandlerRequest>
{
  static const char* value()
  {
    return DataType< ::trajecgenerator::addCSplineTrajecHandler >::value();
  }
  static const char* value(const ::trajecgenerator::addCSplineTrajecHandlerRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::trajecgenerator::addCSplineTrajecHandlerResponse> should match
// service_traits::MD5Sum< ::trajecgenerator::addCSplineTrajecHandler >
template<>
struct MD5Sum< ::trajecgenerator::addCSplineTrajecHandlerResponse>
{
  static const char* value()
  {
    return MD5Sum< ::trajecgenerator::addCSplineTrajecHandler >::value();
  }
  static const char* value(const ::trajecgenerator::addCSplineTrajecHandlerResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::trajecgenerator::addCSplineTrajecHandlerResponse> should match
// service_traits::DataType< ::trajecgenerator::addCSplineTrajecHandler >
template<>
struct DataType< ::trajecgenerator::addCSplineTrajecHandlerResponse>
{
  static const char* value()
  {
    return DataType< ::trajecgenerator::addCSplineTrajecHandler >::value();
  }
  static const char* value(const ::trajecgenerator::addCSplineTrajecHandlerResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TRAJECGENERATOR_MESSAGE_ADDCSPLINETRAJECHANDLER_H