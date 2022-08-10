// Generated by gencpp from file trajecgenerator/addCircleTrajecHandlerResponse.msg
// DO NOT EDIT!


#ifndef TRAJECGENERATOR_MESSAGE_ADDCIRCLETRAJECHANDLERRESPONSE_H
#define TRAJECGENERATOR_MESSAGE_ADDCIRCLETRAJECHANDLERRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace trajecgenerator
{
template <class ContainerAllocator>
struct addCircleTrajecHandlerResponse_
{
  typedef addCircleTrajecHandlerResponse_<ContainerAllocator> Type;

  addCircleTrajecHandlerResponse_()
    {
    }
  addCircleTrajecHandlerResponse_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> const> ConstPtr;

}; // struct addCircleTrajecHandlerResponse_

typedef ::trajecgenerator::addCircleTrajecHandlerResponse_<std::allocator<void> > addCircleTrajecHandlerResponse;

typedef boost::shared_ptr< ::trajecgenerator::addCircleTrajecHandlerResponse > addCircleTrajecHandlerResponsePtr;
typedef boost::shared_ptr< ::trajecgenerator::addCircleTrajecHandlerResponse const> addCircleTrajecHandlerResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace trajecgenerator

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "trajecgenerator/addCircleTrajecHandlerResponse";
  }

  static const char* value(const ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct addCircleTrajecHandlerResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::trajecgenerator::addCircleTrajecHandlerResponse_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // TRAJECGENERATOR_MESSAGE_ADDCIRCLETRAJECHANDLERRESPONSE_H
